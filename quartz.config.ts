import { QuartzConfig } from "./quartz/cfg" 
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration - TTRPG Campaign Theme
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "Boundless and Timeless Wiki",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "en-US",
    baseUrl: "quartz.jzhao.xyz",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "EB Garamond",
        body: "Inter",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#e0e0e0", // Forgotten Grey (Background)
          lightgray: "#c0b9a1", // Aged Parchment
          gray: "#705b5b", // Ancient Ink
          darkgray: "#3b3355", // Planar Violet
          dark: "#1a1a2e", // Deep Void
          secondary: "#c79d3c", // Temporal Gold
          tertiary: "#7a5c99", // Sigil Red (Subtle Purple)
          highlight: "rgba(199, 157, 60, 0.3)",
          textHighlight: "#ffcc00aa",
        },
        darkMode: {
          light: "#1a1a2e", // Deep Void (Background)
          lightgray: "#3b3355", // Planar Violet
          gray: "#5c5470", // Ancient Ink (Darker)
          darkgray: "#9e9cad", // Soft Arcane Glow
          dark: "#e0e0e0", // Text (Bright against dark)
          secondary: "#c79d3c", // Temporal Gold
          tertiary: "#7a5c99", // Sigil Red
          highlight: "rgba(199, 157, 60, 0.3)",
          textHighlight: "#ffcc00aa",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({ priority: ["frontmatter", "git", "filesystem"] }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.NotFoundPage(),
      Plugin.CustomOgImages(),
    ],
  },
}

export default config;
