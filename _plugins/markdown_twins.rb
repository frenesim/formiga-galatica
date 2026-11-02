# frozen_string_literal: true

# Writes a Markdown twin of every HTML page and note, so that agents can read
# the site without parsing HTML (the static-site equivalent of Rails 8.1's
# `format.md`):  /diagnostico-gratuito/  ->  /diagnostico-gratuito.md
#                /                       ->  /index.md
#                /en/                    ->  /en.md
#
# The twin is converted from the same rendered content the HTML page shows
# (before the layout is applied), so both versions always agree.
# Needs a custom plugin, so the site must be built by the GitHub Actions
# workflow (it is), not by GitHub's default Pages build.

require "reverse_markdown"
require "nokogiri"

module MarkdownTwins
  LABELS = {
    "pt" => { contact: "Contacto", email: "Email", phone: "Telefone / WhatsApp", address: "Morada",
              book: "Marcar conversa gratuita", note: "escritório, por marcação",
              published: "Publicado em", alternate: "Versão em inglês", lang: "pt-PT" },
    "en" => { contact: "Contact", email: "Email", phone: "Phone / WhatsApp", address: "Address",
              book: "Book a free call", note: "office, by appointment",
              published: "Published on", alternate: "Portuguese version", lang: "en" }
  }.freeze

  @twins = {}

  class << self
    attr_reader :twins

    def reset!
      @twins = {}
    end

    # "/" -> "index.md", "/en/" -> "en.md", "/notas/x/" -> "notas/x.md"
    def path_for(url)
      return "index.md" if url == "/"

      "#{url.sub(%r{\A/}, '').chomp('/')}.md"
    end

    def eligible?(doc)
      return false if doc.data["sitemap"] == false
      return false unless doc.url.end_with?("/")

      doc.is_a?(Jekyll::Document) ? doc.collection.label == "posts" : !doc.data["layout"].to_s.empty?
    end

    def build(site, doc)
      lang  = doc.data["lang"] == "en" ? "en" : "pt"
      label = LABELS[lang]
      base  = site.config["url"]
      body  = html_to_markdown(site, doc.content, doc.url, lang)
      body  = "# #{doc.data['title']}\n\n#{body}" unless body.start_with?("# ")

      front = ["---", "title: #{doc.data['title'].to_s.inspect}", "url: #{base}#{doc.url}",
               "language: #{label[:lang]}"]
      desc = doc.data["description"] || (doc.url == "/" || doc.url == "/en/" ? site.config["description"] : nil)
      front << "description: #{desc.to_s.inspect}" if desc
      front << "date: #{doc.date.strftime('%Y-%m-%d')}" if doc.is_a?(Jekyll::Document)
      front << "author: #{site.config.dig('author', 'name')}" if doc.is_a?(Jekyll::Document)
      if doc.data["alt_url"]
        alt = twin_url(base, doc.data["alt_url"])
        front << "alternate: #{alt}"
      end
      front << "---"

      "#{front.join("\n")}\n\n#{body}\n\n#{contact_block(site, label)}\n"
    end

    def twin_url(base, url)
      "#{base}/#{path_for(url)}"
    end

    def html_to_markdown(site, html, page_url, lang)
      base = site.config["url"]
      frag = Nokogiri::HTML::DocumentFragment.parse(html)
      frag.css("script, style, form, button, svg, nav, #contacto, .contact").remove
      frag.css("li br").each { |br| br.replace(" ") }
      # "title + text" blocks inside list items read better as bold lead-ins
      frag.css("li > h3").each { |h| h.replace("<strong>#{h.inner_html}.</strong> ") }
      frag.css("a[href]").each do |a|
        href = a["href"]
        if href.start_with?("#")
          # the contact details are appended at the end of every twin; other in-page anchors don't exist in Markdown
          href == "#contacto" ? a["href"] = "##{LABELS[lang][:contact].downcase}" : a.replace(a.children)
        else
          a["href"] = rewrite_link(base, href, page_url)
        end
      end
      frag.css("img[src]").each { |i| i["src"] = rewrite_asset(base, i["src"]) }
      md = ReverseMarkdown.convert(frag.to_html, unknown_tags: :bypass, github_flavored: true)
      md.gsub(/[ \t]+$/, "").gsub(/\n{3,}/, "\n\n").strip
    end

    # internal page links point at the Markdown twin; other URLs just become absolute
    def rewrite_link(base, href, page_url)
      return href if href =~ %r{\A(?:[a-z]+:|//)}i
      return href unless href.start_with?("/")

      path = href.sub(/#.*\z/, "")
      path.end_with?("/") ? "#{base}/#{path_for(path)}" : "#{base}#{path}"
    end

    def rewrite_asset(base, src)
      src.start_with?("/") ? "#{base}#{src}" : src
    end

    def contact_block(site, label)
      c = site.config["company"]
      <<~MD.strip
        ## #{label[:contact]}

        #{c['legal_name']} (NIPC #{c['nipc']})

        - #{label[:email]}: #{c['email']}
        - #{label[:phone]}: #{c['phone']}
        - #{label[:address]}: #{c['street']}, #{c['postal_code']} #{c['locality']} (#{c['city']}), Portugal — #{label[:note]}
        - #{label[:book]}: #{c['calendly']}
      MD
    end
  end
end

Jekyll::Hooks.register :site, :after_reset do |_site|
  MarkdownTwins.reset!
end

Jekyll::Hooks.register %i[pages documents], :post_render do |doc|
  next unless MarkdownTwins.eligible?(doc)

  MarkdownTwins.twins[MarkdownTwins.path_for(doc.url)] = MarkdownTwins.build(doc.site, doc)
end

Jekyll::Hooks.register :site, :post_write do |site|
  MarkdownTwins.twins.each do |path, text|
    dest = File.join(site.dest, path)
    FileUtils.mkdir_p(File.dirname(dest))
    File.write(dest, text)
  end
  Jekyll.logger.info "Markdown:", "wrote #{MarkdownTwins.twins.size} .md twins"
end
