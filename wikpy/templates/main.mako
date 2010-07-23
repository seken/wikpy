<!DOCTYPE html>
<html>
	<head>
		<title>${self.title()} - seken.co.uk</title>
		<script src="/js/script.js" type="text/javascript"></script>
% if c.page.name == 'index':
		<link rel="openid.server" href="http://seken.co.uk/id/" />
		<link rel="openid2.provider" href="http://seken.co.uk/id/" />
% endif
		<link rel="stylesheet" type="text/css" href="/css/style.css" />
	</head>
	<body>
		<nav>
			(<a href="/">home</a> |
			<a href="/special/about">about wiki</a> |
			<a href="/special/${self.title()}/stats">stats</a>
			% if c.links != None:
			${''.join([' | <a href="%s">%s</a>' % i for i in c.links]) | n}
			)
			% endif
			<form action="/special/grep" method="post">
				<input type="text" name="regexp" value="Search" class="searchbox" id="search">
			</form>
		</nav>
		<header>
			<a href="/"><img src="/images/logo.png" border="0" alt="seken" /></a>
		</header>
		<article>
			${self.content()}
		</article>
		<footer>
			<p>Mark Goodall &lt;markit AT seken co uk&gt;. This is a <a href="http://seken.co.uk/Wikpy::">wikpy</a> site.</p>
		</footer>
		
		<script type="text/javascript">
		var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
		document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
		</script>
		<script type="text/javascript">
		try {
		var pageTracker = _gat._getTracker("UA-11781163-1");
		pageTracker._setDomainName("seken.co.uk");
		pageTracker._trackPageview();
		} catch(err) {}</script>
	</body>
</html>