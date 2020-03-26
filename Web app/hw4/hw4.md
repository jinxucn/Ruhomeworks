# Homework 4

###### Jin Xu

###### jx217@scarletmail.rutgers.edu

###### ECE, School of  Graduate Studies

###### Rutgers University

## Q1

### (a)

```dtd
<?xml version="1.0" encoding="UTF-8"?>
<!ELEMENT products (product*)>
<!ELEMENT product (name, price, description, store*)>
<!ELEMENT store (name, phones, markup)>
<!ELEMENT name (#PCDATA)>
<!ELEMENT price (#PCDATA)>
<!ELEMENT description (#PCDATA)>
<!ELEMENT phones (#PCDATA)>
<!ELEMENT markup (#PCDATA)>
<!ATTLIST product pid CDATA #REQUIRED>
<!ATTLIST store sid CDATA #REQUIRED>
```

### (b)

```xquery
<products>
{
    for $product in doc("db.xml")/db/products/row
    return
        <product pid="{$product/pid}">
            {$product/name}{$product/price}{$product/description}
            {
                for $store in doc("db.xml")/db/stores/row
                for $sell in doc("db.xml")/db/sells/row
                where $product/pid = $sell/pid and $store/sid = $sell/sid
                return 
                <store sid="{$store/sid}">
                    {$store/name}{$store/phones}{$sell/markup}
                </store>
            }
        </product>
}
</products>
```

### (c)

```xquery
<products>
{
    for $product in doc("products.xml")/products/product
    where $product/store/markup = "25%"
    return
        <product>
            {$product/name} {$product/price}
        </product>
}
</products>
```

### (d)

```sql
SELECT name, price
FROM products LEFT JOIN sells ON products.pid=sells.pid
WHERE markup=0.25
GROUP BY name
```

## Q2

### (a)

```xquery
for $title in doc("q2.xml")/broadway//title
	return
        <titles>
    		{$title}
    	</titles>
```

### (b)

```xquery
for $theater doc("q2.xml")/broadway/theater[date = "11/9/2008"]
where some $price in $theater/price satisfies data($price) < 35
	return
		<theaters>
      		{$theater/title}{$theater/address}
    	</theaters
```

### (c)

```xquery
for $concert in doc("q2.xml")/broadway/concert[type = "chamber orchestra"]
where avg(data($concert/price))>=50
	return
		<concerts>
			{$x/title}
		</concerts>
```

### (d)

```xquery
  
for $date in distinct-values(doc("q2.xml")//date)
  for $s in //theater[date = $date] | //concert[date = $date] | //opera[date=$date]
    return
      <groupByDate>
            <day>
              {$date}
              <show>
                {$s/title}
                {$s/price}
              </show>
            </day>
      </groupByDate>
```

## Q3

### (1)

In XSL:

```xml-dtd
<xsl:for-each select="bib/book"> 
    <p/><li>
        <xsl:value-of select="author/last_name"/>,
        <xsl:value-of select="author/first_name"/>.
        <b><xsl:value-of select="title"/></b> 
        (<xsl:value-of select="publisher"/>
        <xsl:text> </xsl:text>
        <xsl:value-of select="address"/>
        <xsl:text> </xsl:text>
        <xsl:value-of select="year"/>).
    </li> 
</xsl:for-each>

<xsl:for-each select="bib/article"> 
    <p/><li>
        <xsl:value-of select="author/last_name"/>,
        <xsl:value-of select="author/first_name"/>. 
        <xsl:value-of select="title"/>, 
        <b><xsl:value-of select="journal"/>, 
        <xsl:value-of select="volume"/></b>, 
        pp.<xsl:apply-templates select="page"/> 
        <xsl:value-of select="year"/>.
    </li> 
</xsl:for-each>
```

In XML:

```xml
change
<author>Leslie Lamport</author>
to
<author>
    <first_name>Leslie</first_name>
    <last_name>Lamport</last_name>
</author>
etc.
```

### (2)

```xml
<book>
    <author>
        <first_name>First1</first_name>
        <last_name>Last1</last_name>
    </author>
    <title>This is a book1</title>
    <year>2005</year>
    <address>NJ</address>
    <publisher>A-Publisher</publisher>
</book>

<book>
    <author>
        <first_name>First2</first_name>
        <last_name>Last2</last_name>
    </author>
    <title>A book without publisher</title>
    <year>2014</year>
</book>

<article>
    <author>
        <first_name>Best</first_name>
        <last_name>Writer</last_name>
    </author>
    <title>This is an article</title>
    <year>2012</year>
    <volume>54</volume>
    <page>
        <from>452</from>
        <to>501</to>
    </page>
    <journal>Best journal</journal>
</article>

<article>
    <author>
        <first_name>Worst</first_name>
        <last_name>Writer</last_name>
    </author>
    <title>An article without volume</title>
    <year>2015</year>
    <page>
        <from>23</from>
        <to>87</to>
    </page>
    <journal>Best journal</journal>
</article>
```

### (3)

In XSL:

```xml-dtd
<xsl:for-each select="bib/phd_theses"> <p/>
    <li>
        <xsl:value-of select="author/last_name"/>,
        <xsl:value-of select="author/first_name"/>. 
        <b><xsl:value-of select="title"/></b>, 
        <xsl:value-of select="year"/>, 
        <em><xsl:value-of select="school"/></em>.
    </li>
</xsl:for-each>
```

In XML:

```xaml
<phd_theses>
    <author>
        <first_name>Best</first_name>
        <last_name>Student</last_name>
    </author>
    <title>The best thesis ever</title>
    <year>2004</year>
    <school>Biographic school</school>
</phd_theses>

<phd_theses>
    <author>
        <first_name>Worst</first_name>
        <last_name>Student</last_name>
    </author>
    <title>The worst thesis ever</title>
    <year>2004</year>
    <school>Biographic school</school>
</phd_theses>
```

