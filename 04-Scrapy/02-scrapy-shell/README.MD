# scrapy
## scrapy instalacion

Ejecutar dentro del `Anaconda prompt`.
```
$ pip install scrapy
```

## Comandos geenerales

Da `las caracteristicas` para poder hacer web Scraping o Web Crealing de ese computador
```
$ scrapy bench
```
Visualizar las `configuraciones extra`
```
$ scrapy settings
```
Visualizamos la `version` de Scrapy
```
$ scrapy version
```

## Scrapy view `url`

Aqui se puede ver un ejemplo:
```
$ scrapy view https://www.pluralsight.com/authors
```

No se ve el contenido de esta pagina por que hay servidores que redireccionan a javaScript y no se puede hacer scrapy
```
$ scrapy view https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT
```

### scrapy shell `url`

Permite `interactual con la respuesta` del scrapy medianye un `shell`
```
$ scrapy shell http://quotes.toscrape.com/page/1/
```
no da una shell de python listo para usar

```
$ response.css('title')
```

```
response.css('title').extract()
```

```
$ response.css('title::text').extract()
```

```
$ response.css('.tags .tag::text').extract()
```

```
$ response.css('div.tags > a.tag::attr(href)').extract()
```
```
$ response.css('.row > div > div:nth-child(2) > .text::text').extract()

```
```
$ response.xpath("/html/body/div/div[2]/div[2]/h2").extract_first()
```
```
$ response.xpath("//div[@class='quote']/span/a/@href").extract_first()
```
```
$ response.css('div.tags > a.tag::attr(href)').extract()
```

## Scrapy startproject `nombre_proyecto`
```
$ scrapy startproject arania_basica
```
