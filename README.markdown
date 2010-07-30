# wikpy

Wikpy is an open source wiki written using the [pylons](http://pylonshq.com/) framework. The page syntax is in [Markdown](http://daringfireball.net/projects/markdown/syntax) using the markdown2 package.

## Installation instructions

wikpy is available on pypi, so you can use `easy_install wikpy` to install it.

You can then follow [these instructions](http://pylonshq.com/docs/en/1.0/deployment/#understanding-the-setup-process) by pylons to construct the database and configuration options in a directory. For example:

    $ paster make-config wikpy wikpy_production.ini
    $ paster setup-app wikpy_production.ini

To serve the wiki using paster, you can run `paster serve wikpy_production.ini`. However, a better method would be to serve via Apache2 using the [mod_wsgi](http://code.google.com/p/modwsgi/) module. An example apache vhost configuration would be as follows:

    WSGIDaemonProcess <AProcessName> user=<ValidUsername> home=<LocationOfDatabaseAndConfigFolder>
	WSGIProcessGroup <AProcessName>
	WSGIScriptAlias /wiki <PathTo wikpy.wsgi>

Optionally, if you use wikpy as the root (/) application for a vhost then you can override the default css, images, etc using the apache [alias directive](http://httpd.apache.org/docs/2.0/mod/mod_alias.html#alias).

Additionally, to add OpenID authentication to wikpy currently you could use [mod_auth_openid](http://trac.butterfat.net/public/mod_auth_openid). Authentication can be added to the edit and save pages by adding to the apache vhost config for the wiki as follows:

    <LocationMatch "edit">
    	AuthOpenIDEnabled On
    	AuthOpenIDDBLocation <LocationOfAuthDB>
    	AuthOpenIDTrusted <Trusted>
    	AuthOpenIDTrustRoot <TrustedRoot>
    </LocationMatch>
    <LocationMatch "save">
    	AuthOpenIDEnabled On
    	AuthOpenIDDBLocation <LocationOfAuthDB>
    	AuthOpenIDTrusted <Trusted>
    	AuthOpenIDTrustRoot <TrustedRoot>
    </LocationMatch>

