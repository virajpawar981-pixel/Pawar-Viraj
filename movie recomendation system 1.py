export default function MovieRecommendationWebsite() {
  const movies = [
    {
      title: "Inception",
      genre: "Sci‑Fi / Thriller",
      rating: "8.8",
      image:
        "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?q=80&w=1200&auto=format&fit=crop",
      description:
        "A mind-bending journey through dreams and reality directed by Christopher Nolan.",
    },
    {
      title: "Interstellar",
      genre: "Sci‑Fi / Adventure",
      rating: "8.7",
      image:
        "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?q=80&w=1200&auto=format&fit=crop",
      description:
        "A team of explorers travels through a wormhole in space to save humanity.",
    },
    {
      title: "The Dark Knight",
      genre: "Action / Crime",
      rating: "9.0",
      image:
        "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?q=80&w=1200&auto=format&fit=crop",
      description:
        "Batman faces the Joker in one of the greatest superhero movies ever made.",
    },
    {
      title: "Avengers: Endgame",
      genre: "Action / Superhero",
      rating: "8.4",
      image:
        "https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=1200&auto=format&fit=crop",
      description:
        "Marvel heroes unite for the final battle against Thanos.",
    },
    {
      title: "Joker",
      genre: "Drama / Thriller",
      rating: "8.4",
      image:
        "https://images.unsplash.com/photo-1513106580091-1d82408b8cd6?q=80&w=1200&auto=format&fit=crop",
      description:
        "A dark psychological story about the rise of Gotham's infamous villain.",
    },
    {
      title: "Titanic",
      genre: "Romance / Drama",
      rating: "7.9",
      image:
        "https://images.unsplash.com/photo-1478720568477-152d9b164e26?q=80&w=1200&auto=format&fit=crop",
      description:
        "A timeless love story set during the tragic sinking of the Titanic.",
    },
  ];

  return (
    <div className="min-h-screen bg-black text-white">
      {/* Header */}
      <header className="bg-gradient-to-r from-red-700 via-black to-red-900 p-6 shadow-2xl">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-4">
          <h1 className="text-4xl font-extrabold tracking-wide">
            🎬 Movie Recommendation Hub
          </h1>

          <input
            type="text"
            placeholder="Search movies..."
            className="px-4 py-2 rounded-xl text-black w-full md:w-72 outline-none"
          />
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative h-[400px] flex items-center justify-center text-center overflow-hidden">
        <img
          src="https://images.unsplash.com/photo-1518929458119-e5bf444c30f4?q=80&w=1600&auto=format&fit=crop"
          alt="Cinema"
          className="absolute inset-0 w-full h-full object-cover opacity-40"
        />

        <div className="relative z-10 px-6">
          <h2 className="text-5xl md:text-6xl font-bold mb-4">
            Discover Amazing Movies
          </h2>
          <p className="text-lg md:text-xl text-gray-300 max-w-2xl mx-auto">
            Find top-rated movies from different genres and enjoy your perfect movie night.
          </p>

          <button className="mt-6 bg-red-600 hover:bg-red-700 transition px-6 py-3 rounded-2xl text-lg font-semibold shadow-lg">
            Explore Now
          </button>
        </div>
      </section>

      {/* Movie Cards */}
      <section className="max-w-7xl mx-auto px-6 py-14">
        <div className="flex items-center justify-between mb-8">
          <h3 className="text-3xl font-bold">Top Recommendations</h3>

          <select className="bg-gray-900 border border-gray-700 px-4 py-2 rounded-xl">
            <option>All Genres</option>
            <option>Action</option>
            <option>Sci‑Fi</option>
            <option>Drama</option>
            <option>Romance</option>
          </select>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          {movies.map((movie, index) => (
            <div
              key={index}
              className="bg-gray-900 rounded-3xl overflow-hidden shadow-2xl hover:scale-105 transition duration-300"
            >
              <img
                src={movie.image}
                alt={movie.title}
                className="w-full h-72 object-cover"
              />

              <div className="p-5">
                <div className="flex justify-between items-center mb-2">
                  <h4 className="text-2xl font-bold">{movie.title}</h4>
                  <span className="bg-yellow-500 text-black px-3 py-1 rounded-full text-sm font-bold">
                    ⭐ {movie.rating}
                  </span>
                </div>

                <p className="text-red-400 font-medium mb-3">{movie.genre}</p>

                <p className="text-gray-300 text-sm leading-relaxed">
                  {movie.description}
                </p>

                <button className="mt-5 w-full bg-red-600 hover:bg-red-700 transition py-2 rounded-xl font-semibold">
                  Watch Trailer
                </button>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-950 border-t border-gray-800 py-6 text-center text-gray-400">
        <p>© 2026 Movie Recommendation Hub. All Rights Reserved.</p>
      </footer>
    </div>
  );
}