import redis

def test_gitlab_ci_redis_access():
    r = redis.Redis(
        host='redis',
        port=6379,
        db=0,
        encoding="utf-8",
        decode_responses=True)

    r.set('foo', 'bar')

    assert r.get('foo') == 'bar'


