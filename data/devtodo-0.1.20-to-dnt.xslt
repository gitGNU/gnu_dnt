<xsl:stylesheet version="1.0"
		xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <!-- Output settings -->
  <xsl:output method="xml"
	      omit-xml-declaration="no"
	      indent="yes"/>

  <!-- Global variables -->
  <xsl:variable name="newLine">
    <xsl:text>
    </xsl:text>
  </xsl:variable>

  <!-- Main -->
  <xsl:template match="/todo">
    <root>
      <xsl:if test="/todo/title">
	<xsl:value-of select="/todo/title"/>
      </xsl:if>
      <xsl:for-each select="child::*">
	<xsl:if test="name() = 'note'">
	  <xsl:call-template name="nodeProcess"/>
	</xsl:if>
      </xsl:for-each>
    </root>
  </xsl:template>

  <!-- SubNodes Process  -->
  <xsl:template name="subnodesProcess">
    <xsl:for-each select="child::*">
      <xsl:if test="name() = 'note'">
	<xsl:call-template name="nodeProcess"/>
      </xsl:if>
    </xsl:for-each>
  </xsl:template>

  <!-- Node Process -->
  <xsl:template name="nodeProcess">
    <entry>
      <xsl:if test="@done">
	<xsl:attribute name="end">
	  <xsl:value-of select="@done"/>
	</xsl:attribute>
      </xsl:if>
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
      <xsl:value-of select="text()"/>
      <xsl:if test="@done">
	<xsl:if test="comment">
	  <comment>
	    <xsl:variable name="c">
	      <xsl:value-of select="comment"/>
	    </xsl:variable>
	    <xsl:value-of select="$c"/>
	  </comment>
	</xsl:if>
      </xsl:if>
      <xsl:call-template name="subnodesProcess"/>
    </entry>
    <xsl:value-of select="$newLine"/>
  </xsl:template>
</xsl:stylesheet>
