def analisa_review(ratings):
    min_rating = min(ratings)
    max_rating = max(ratings)
    avg_rating = sum(ratings) / len(ratings)

    return [min_rating, max_rating, avg_rating]

print(analisa_review([4.5, 2.0, 1.5, 3.0, 2.5, 4.0, 5.0, 3.5, 2.0, 1.0]))
print(analisa_review([5,4,2.5,5,3.6,1.1,3.6,4,4.2,1.5]))
