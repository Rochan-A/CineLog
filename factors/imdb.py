from imdbpie import Imdb
import sys

def calc(s):
	imdb = Imdb()
	imdb = Imdb(anonymize=True) # to proxy requests
	names = imdb.search_for_title(s)
	title = imdb.get_title_by_id(names[0][u'imdb_id'])
	#d = title.title + title.imdb_id + title.type + title.year + title.rating + title.genres + title.votes, title.runtime, title.release_date, title.cast_summary
	return str(title.title)

#print calc(sys.argv[1])
