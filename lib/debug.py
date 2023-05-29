#!/usr/bin/env python3
import ipdb;
from Article import Article
from Author import Author
from Magazine import Magazine

if __name__ == '__main__':


    # Create instances of Article, Author, and Magazine

    # Articles
    article1 = Article("Kenyan Wildlife Conservation", "Exploring the rich biodiversity of Kenya's national parks.")
    article2 = Article("African Art and Culture", "Unveiling the beauty and significance of African traditional art.")
    article3 = Article("Discovering Maasai Culture", "An in-depth look into the traditions and customs of the Maasai people.")
    article4 = Article("Safari Adventures in Kenya", "Embark on a thrilling safari journey through Kenya's national reserves.")
    article5 = Article("Exploring Swahili Cuisine", "Delicious flavors and traditional dishes of the Swahili coastal region.")
    article6 = Article("Mount Kenya: The Roof of Africa", "Scaling the majestic peaks of Mount Kenya.")
    article7 = Article("Preserving African Heritage", "Efforts to safeguard African artifacts and cultural heritage.")
    article8 = Article("Ecotourism in Kenya", "Promoting sustainable tourism practices for conservation and community development.")
    article9 = Article("The Great Wildebeest Migration", "Witness the epic migration of wildebeests across the Maasai Mara.")
    article10 = Article("Kenyan Contemporary Art", "Exploring the vibrant and dynamic art scene in Kenya.")

    # Authors
    author1 = Author("Wangari Maathai")
    author2 = Author("Ngũgĩ wa Thiong'o")
    author3 = Author("Binyavanga Wainaina")
    author4 = Author("Meja Mwangi")
    author5 = Author("Yvonne Adhiambo Owuor")
    author6 = Author("Peter Kimani")
    author7 = Author("Grace Ogot")
    author8 = Author("Mukoma wa Ngugi")
    author9 = Author("Marjorie Oludhe Macgoye")
    author10 = Author("Nuruddin Farah")

    # Magazines
    magazine1 = Magazine("news", "Kenya Today", [article1, article2], [author1, author2])
    magazine2 = Magazine("lifestyle", "African Explorer", [article3, article4], [author3, author4])
    magazine3 = Magazine("lifestyle", "Safari Lifestyle", [article5, article6], [author5, author6])
    magazine4 = Magazine("business", "Africa Today", [article7, article8], [author7, author8])
    magazine5 = Magazine("travel", "Wilderness Explorer", [article9, article10], [author9, author10])

    # Display the magazine details
    magazine1.display()
    magazine2.display()
    magazine3.display()
    magazine4.display()
    
    magazine5.display()

# DO NOT REMOVE THIS
    ipdb.set_trace()
