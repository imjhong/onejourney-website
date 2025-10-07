<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9">
<xsl:output method="html" encoding="UTF-8" indent="yes"/>
<xsl:template match="/">
  <html>
    <head>
      <title>XML Sitemap</title>
      <style>
        body { font-family: sans-serif; color: #333; }
        table { border-collapse: collapse; width: 100%; }
        th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #f2f2f2; }
        a { color: #0077cc; text-decoration: none; }
        a:hover { text-decoration: underline; }
      </style>
    </head>
    <body>
      <h1>XML Sitemap</h1>
      <p>This sitemap was generated to be read by search engines.</p>
      <table>
        <tr>
          <th>URL Location</th>
          <th>Last Modified</th>
        </tr>
        <xsl:for-each select="sitemap:urlset/sitemap:url">
          <tr>
            <td>
              <xsl:variable name="loc" select="sitemap:loc"/>
              <a href="{$loc}"><xsl:value-of select="$loc"/></a>
            </td>
            <td>
              <xsl:value-of select="sitemap:lastmod"/>
            </td>
          </tr>
        </xsl:for-each>
      </table>
    </body>
  </html>
</xsl:template>
</xsl:stylesheet>