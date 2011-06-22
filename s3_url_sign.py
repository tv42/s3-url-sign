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

    conn_kwargs = {}
    host = boto.config.get('Boto', 's3_host')
    if host is not None:
        conn_kwargs['host'] = host
    port = boto.config.getint('Boto', 's3_port')
    if port is not None:
        conn_kwargs['port'] = port
    conn = boto.s3.connection.S3Connection(
        calling_format=boto.s3.connection.OrdinaryCallingFormat(),
        **conn_kwargs
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
