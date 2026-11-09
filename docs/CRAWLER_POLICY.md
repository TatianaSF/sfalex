# Crawler policy

The production `robots.txt` allows public crawling and advertises the sitemap. It intentionally has no per-vendor AI crawler directives. This preserves ordinary search access and does not create new training permissions or restrictions.

Crawler products and user-fetch agents have different purposes and may use distinct user-agent tokens. Robots rules are requests to compliant crawlers, not access control. The `llms.txt` and Markdown summaries are convenience documents; they do not guarantee discovery, citation, or model behavior. Private material must never be placed in the public artifact.

References: [Google robots.txt guidance](https://developers.google.com/search/docs/crawling-indexing/robots/intro), [OpenAI crawler documentation](https://platform.openai.com/docs/bots), [Anthropic web crawler guidance](https://docs.anthropic.com/en/docs/about-claude/claude-on-the-web), and [Perplexity crawler FAQ](https://docs.perplexity.ai/guides/bots).
