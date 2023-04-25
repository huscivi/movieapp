from django.shortcuts import render

kategori_listesi = ["macera", "romantik", "dram"]
film_listesi = [
    {
    "film_adi" : "film1",
    "aciklama": "film 1 aciklamasi",
    "resim": "https://picsum.photos/200/300?random=1"
    },
    {
    "film_adi" : "film2",
    "aciklama": "film 2 aciklamasi",
    "resim": "https://picsum.photos/200/300?random=2"
    },
    {
    "film_adi" : "film3",
    "aciklama": "film 3 aciklamasi",
    "resim": "https://picsum.photos/200/300?random=3"
    }    
]

def home(request):
    data = {
        "kategoriler": kategori_listesi,
        "filmler": film_listesi
    }

    return render(request, "index.html", data)

def movies(request):
    return render(request, "movies.html")