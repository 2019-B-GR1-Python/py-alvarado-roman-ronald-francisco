import scrapy
import pandas as pd

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'    
    images_url = []
    title = []
    price = []    
    
    def start_requests(self):
        for i in range(1,51):
            self.urls = [f'http://books.toscrape.com/catalogue/category/books_1/page-{i}.html']
            for url in self.urls:
                yield scrapy.Request(url=url)

    def parse(self, response):
        etiqueta_contenedora = response.css('article.product_pod')
        titulos = etiqueta_contenedora.css('h3 > a::text').extract()
        precios = etiqueta_contenedora.css('div > p.price_color::text').extract()
        url_imagenes = etiqueta_contenedora.css('h3 > a::attr(href)').extract()
        for i in range(len(titulos)):
            self.images_url.append(response.urljoin(url_imagenes[i]))
            self.title.append(titulos[i])
            self.price.append(precios[i])
        
        
        #print(self.title)

        S_titulo = pd.Series(self.title)
        #S_urlImagenes = pd.Series(url_imagenes)
        S_urlImagenes = pd.Series(self.images_url)
        S_precios = pd.Series(self.price)

        df = pd.DataFrame({"Titulos": S_titulo, "Url's Imagenes": S_urlImagenes, "Precio": S_precios})
        print(f'df {df}')
        
        path_guardado = './DatosLibro1.xlsx'
        df_Libro = df.copy()
        df_Libro.to_excel(path_guardado, index = True)