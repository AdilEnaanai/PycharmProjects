import datetime
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
pd.set_option('display.max_columns',None)
driver = webdriver.Chrome()
annonces=pd.DataFrame()
for i in range(1,2):
    driver.get("https://www.marocannonces.com/maroc/telephones-portables--b359.html?pge="+str(i))

    soup=BeautifulSoup(driver.page_source,"html.parser")
    blocs=soup.select("ul.cars-list>li")

    for bloc in blocs:
        annonce={}
        titre=bloc.select_one("div.holder>h3")
        prix= bloc.select_one("div.holder>strong.price")
        ville = bloc.select_one("div.holder>span.location")
        dateheure = bloc.select_one("em.date")
        annonce['titre']=titre.text.strip() if titre is not None else ""
        annonce['prix'] = prix.text.strip() if prix is not None else ""
        annonce['ville'] = ville.text.strip() if ville is not None else ""
        annonce['dateheure'] = dateheure.text.strip() if dateheure is not None else ""
        annonces=annonces.append(annonce,ignore_index=True)
annonces['prix']=annonces['prix'].map(lambda p:''.join([i for i in p if i.isdigit()]))
annonces['dateheure']=annonces['dateheure'].str.replace('Hier',(datetime.date.today()-datetime.timedelta(1)).strftime("%d %b %Y "))
#annonces['dateheure']=annonces['dateheure'].map(lambda d:str(d).replace('Hier'))

annoncesParville=annonces.groupby('ville').agg(Nombre_annonces=('titre','count')).reset_index()
annoncesParville=annoncesParville.query("ville!=''")
#print(annoncesParville)

plt.bar(annoncesParville['ville'],annoncesParville['Nombre_annonces'])
plt.xticks(rotation=45)
plt.show()
