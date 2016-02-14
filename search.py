def get_page(url):
	try:
	   import urllib
	   return urllib.urlopen(url).read()
	except:
	   return ''


def find_link(page, startpos):
	link_start = page.find('<a href=', startpos)
	start_qoute = page.find('"', link_start)
	end_qoute = page.find('"', start_qoute + 1)
	url = page[start_qoute + 1 : end_qoute]
	return url, link_start

def get_all_links(page):
	endpos = 0
	while True:
	     url, endpos = find_link(page, endpos + 1)
	     if endpos == -1:
		break

	     print url
		


get_all_links(get_page('http://www.github.com'))
#get_all_links('shgshgfhjsdg<a href="facebook.com">link</a>fhjsdg<a href="youtube.com">link</a>shgfhjsdg<a href="google.com">link</a>')
