from collections import defaultdict

def solution(genres, plays):
    genre_play_count = defaultdict(int)
    song_data = defaultdict(list)

    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_play_count[genre] += play
        song_data[genre].append((play, i))

    sorted_genres = sorted(genre_play_count.keys(), key=lambda g: genre_play_count[g], reverse=True)

    best_album = []

    for genre in sorted_genres:
        sorted_songs = sorted(song_data[genre], key=lambda x: (-x[0], x[1]))
        best_album.extend([song[1] for song in sorted_songs[:2]])

    return best_album