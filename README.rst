======================================================
 S3-URL-Sign -- easy way to sign URLs for use with S3
======================================================

To get started, type::

	./bootstrap

Set up your ``~/.boto`` config file, something like::

	[Credentials]
	aws_access_key_id = EDIT-ME
	aws_secret_access_key = EDIT-ME

And then run (replace ``BUCKET`` and ``OBJECT`` as appropriate)::

	./virtualenv/bin/s3-url-sign BUCKET
	./virtualenv/bin/s3-url-sign BUCKET OBJECT

Some more examples::

	$ wget -q -O- "$(./virtualenv/bin/s3-url-sign BUCKET)"|xmlstarlet fo|head -3
	<?xml version="1.0" encoding="UTF-8"?>
	<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
	  <Name>BUCKET</Name>

	$ wget -O SOMETHING "$(./virtualenv/bin/s3-url-sign BUCKET OBJECT)"
	--2011-06-21 12:40:15--  https://BUCKET.s3.amazonaws.com/OBJECT?Signature=...&Expires=...&AWSAccessKeyId=...
	Resolving BUCKET.s3.amazonaws.com... 207.171.187.118
	Connecting to BUCKET.s3.amazonaws.com|207.171.187.118|:443... connected.
	HTTP request sent, awaiting response... 200 OK
	Length: 10888 (11K) [application/x-object]
	Saving to: `SOMETHING'
	
	100%[=========================================================>] 10,888      --.-K/s   in 0s      
	
	2011-06-21 12:40:15 (39.3 MB/s) - `SOMETHING' saved [10888/10888]
