<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output xsl:method="text"
              xsl:indent="yes"/>

  <!-- Main -->
  <xsl:template match="/">
    <root>
      <xsl:variable name="title" select="todo/title"/>
      <xsl:choose>
	<xsl:when xsl:test = '$title=""'>
	  TODO list
	</xsl:when>
	<xsl:otherwise>
	  <xsl:value-of select="todo/title"/>
	</xsl:otherwise>
      </xsl:choose>
      <xsl:call-template name="noteList"/>
    </root>
  </xsl:template>

  <!-- Note List -->
  <xsl:template name="noteList">
    <xsl:for-each select="todo/note">
      <xsl:call-template name="noteItem"/>
    </xsl:for-each>
  </xsl:template>

  <!-- Note Item -->
  <xsl:template name="noteItem">
    <xsl:apply-templates select="."/>
  </xsl:template>

  <!-- Note -->
  <xsl:template match="note">
    <entry>

      <xsl:if test="@priority">
        <xsl:attribute name="priority">
          <xsl:value-of select="@priority"/>
        </xsl:attribute>
      </xsl:if>

      <xsl:if test="@time">
        <xsl:attribute name="start">
          <xsl:value-of select="@time"/>
        </xsl:attribute>
      </xsl:if>

      <xsl:if test="@done">
        <xsl:attribute name="end">
          <xsl:value-of select="@done"/>
        </xsl:attribute>
      </xsl:if>

      <xsl:value-of select="child::text()"/>

      <xsl:for-each select="./note">
        <xsl:call-template name="noteItem"/>
      </xsl:for-each>

    </entry>
  </xsl:template>

</xsl:stylesheet>
