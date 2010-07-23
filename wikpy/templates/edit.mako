<%inherit file="main.mako"/>
<%def name="title()">editing ${c.page.name}</%def>
<%def name="content()">
<form action="/save/${c.page.fullname()}" method="post">
	<p><label for="tags">Tags</label><input type="text" name="tags" value="${''.join([x.name+',' for x in c.page.tags])}"/></p>
	<p><label for="text">Page Content</label><textarea name="text" id="editor">${c.page.text}</textarea></p>
	<p><input type="submit" value="save"/></p>
</form>
</%def>