import boto.s3.connection
import optparse

def main():
    parser = optparse.OptionParser(
        usage='%prog BUCKET [KEY]',
        )
    parser.add_option(
        '--method',
        default='GET',
        help='HTTP method to use [default: %default]',
        )
    parser.add_option(
        '--expiry',
        type='int',
        default=60*60*24,
        help='seconds before expiry [default: %default]',
        )
    opts, args = parser.parse_args()
    try:
        (bucket, key) = args
    except ValueError:
        try:
            (bucket,) = args
        except ValueError:
            parser.error('Unexpected arguments.')
        else:
            key = None

    conn = boto.s3.connection.S3Connection(
        # aws_access_key_id=cfg.get(section, 'access_key'),
        # aws_secret_access_key=cfg.get(section, 'secret_key'),
        # is_secure=cfg.getboolean(section, 'is_secure'),
        # port=port,
        # host=cfg.get(section, 'host'),
        )
    kwargs = {}
    if bucket is not None:
        kwargs['bucket'] = bucket
    if key is not None:
        kwargs['key'] = key
    url = conn.generate_url(
        expires_in=opts.expiry,
        method=opts.method,
        **kwargs
        )
    print url
