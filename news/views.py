from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup as BSoup
from news.models import Headline

def scrape(request, name):
    from django.shortcuts import redirect
    import requests
    from bs4 import BeautifulSoup as BSoup
    from news.models import Headline

    print("SCRAPING STARTED FOR:", name)
    Headline.objects.all().delete()

    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    url = f"https://indianexpress.com/section/{name}/"
    print("URL TO SCRAPE:", url)

    response = session.get(url)
    soup = BSoup(response.content, "html.parser")

    articles = soup.find_all("div", class_="articles")
    if not articles:
        articles = soup.find_all("div", class_="nation") or soup.find_all("div", class_="top-news") or soup.find_all("div", class_="other-articles")

    print(f"Found {len(articles)} articles")

    for article in articles:
        link_tag = article.find("a", href=True)
        link = link_tag["href"] if link_tag else None

        title_tag = article.find("h2") or article.find("h3")
        title = title_tag.text.strip() if title_tag else None

        # Improved image handling
        img_tag = article.find("img")
        img = None

        if img_tag:
            img = (
                img_tag.get("data-lazy-src") or
                img_tag.get("data-src") or
                img_tag.get("data-lazy") or
                img_tag.get("src") or
                img_tag.get("data-srcset")
            )

        # Handle <picture> or <source> tags
        if not img:
            source_tag = article.find("source")
            if source_tag and source_tag.get("data-srcset"):
                img = source_tag.get("data-srcset").split()[0]  # Take the first image URL

        if not img:
            img = "https://via.placeholder.com/300x200?text=No+Image"

        if link and title:
            Headline.objects.create(title=title, url=link, image=img)

    return redirect("home")


def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {"object_list": headlines}
    return render(request, "news/home.html", context)
