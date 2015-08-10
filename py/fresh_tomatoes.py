import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        /*Additional styling for background image and container title*/
        .bgimage {
            background-origin: content-box;
            background-image: url("../images/background_image.jpg");
            background-position: top;
            background-size: cover;
            background-repeat: no-repeat;
            height: 400px;
        }
        .text-title {
            margin-top: 50px;
            margin-bottom: 0px;
            text-align: center;
        }
    </style>
    
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile, .bgimage', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
            
            //Get movie title and display it on a specific paragragh in the modal
            var movieTitle = $(this).attr('data-movie-title');
            movieTitle = 'Title: ' + movieTitle;
            $("#movie-title").text(movieTitle);
            
            //Get movie release year and display it on a specific paragragh in the modal
            var movieReleaseYear = $(this).attr('data-movie-release-year');
            movieReleaseYear = 'Release Year: ' + movieReleaseYear;
            $("#movie-release-year").text(movieReleaseYear);
            
            //Get movie rating and display it on a specific paragragh in the modal
            var movieRating = $(this).attr('data-movie-rating');
            movieRating= 'Rating: ' + movieRating;
            $("#movie-rating").text(movieRating);
            
            //Get movie storyline and display it on a specific paragragh in the modal
            var movieStoryline = $(this).attr('data-movie-storyline');
            movieStoryline = 'Storyline: ' + movieStoryline;
            $("#movie-storyline").text(movieStoryline);
            
            //Get movie director and display it on a specific paragragh in the modal
            var movieDirector = $(this).attr('data-movie-director');
            movieDirector = 'Director: ' + movieDirector;
            $("#movie-director").text(movieDirector);
            
            //Get movie stars and display it on a specific paragragh in the modal
            var movieStars = $(this).attr('data-movie-stars');
            movieStars = 'Stars: ' + movieStars;
            $("#movie-stars").text(movieStars);
        });
        //Commenting out animation of movies on page load
        // Animate in the movies when the page loads
        //$(document).ready(function () {
          //$('.movie-tile').hide().first().show("fast", function showNext() {
            //$(this).next("div").show("fast", showNext);
          //});
        //});
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
 
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
        <div class="modal-dialog">
            <div class="modal-content">
                <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
                </a>
                <div class="scale-media" id="trailer-video-container">
                </div>
                <!-- Add div in modal to display additional movie information -->
                <div>
                  <p id="movie-title" style="padding-left: 20px; padding-right: 20px; padding-top: 20px;">Title:</p>
                  <p id="movie-release-year" style="padding-left: 20px; padding-right: 20px;">Release Year:</p>
                  <p id="movie-rating" style="padding-left: 20px; padding-right: 20px;">Rating:</p>
                  <p id="movie-storyline" style="padding-left: 20px; padding-right: 20px;">Storyline:</p>
                  <p id="movie-director" style="padding-left: 20px; padding-right: 20px;">Director:</p>
                  <p id="movie-stars" style="padding-left: 20px; padding-right: 20px; padding-bottom: 10px;">Stars:</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <!-- Add container for background image of #1 movie pick on top of page -->
    <div class="container">
      <div class="row">
        <!-- In div tag, include movie information / data that will be passed into the modal target on click action -->
        <div class="col-md-12 bgimage text-right" data-trailer-youtube-id="5PSNL1qE6VY" data-movie-title="Avatar" data-movie-release-year="2009" data-movie-rating="PG-13" data-movie-storyline="A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home." data-movie-director="James Cameron" data-movie-stars="Sam Worthington, Zoe Saldana, Sigourney Weaver" data-toggle="modal" data-target="#trailer">
            <p style="padding-right: 40px; padding-top: 80px; font-size: 30px; color: #F5F5F5;"><i>#1 Pick:</i></p>
            <p style="padding-right: 40px; font-size: 36px; color: #F5F5F5;">Avatar (2009)</p>
            <p style="padding-right: 40px; font-size: 24px; color: #F5F5F5;">Rated PG-13</p>
            <p style="padding-right: 40px; font-size: 18px; color: #F5F5F5;">Sam Worthington, Zoe Saldana</p>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <h2 class="text-title">Top Movie Picks</h2>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <hr>
        </div>
      </div>
      {movie_tiles}
      <div class="row">
        <div class="col-md-12 col-xs-12">
          <hr style="padding-bottom: 50px;">
        </div>
      </div>
    </div>
  </body>
</html>
'''

# A single movie entry html template. Its div tag includes movie information / data that will be passed into the modal target on click action
movie_tile_content = '''
<div class="col-sm-6 col-md-4 col-lg-3 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-movie-title="{movie_title}" data-movie-release-year="{movie_release_year}" data-movie-rating="{movie_rating}" data-movie-storyline="{movie_storyline}" data-movie-director="{movie_director}" data-movie-stars="{movie_stars}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="330">
    <h2>{movie_title}</h2>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in. Content has been extended to include all movie related information
        content += movie_tile_content.format(
            movie_title = movie.title,
            movie_release_year = movie.release_year,
            movie_rating = movie.rating,
            movie_storyline = movie.storyline,
            movie_director = movie.director,
            movie_stars = movie.stars,
            poster_image_url = movie.poster_image_url,
            trailer_youtube_id = trailer_youtube_id
        )
    return content


def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible