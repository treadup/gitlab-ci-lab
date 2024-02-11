import memcache

def test_gitlab_ci_memcached_access():
    mc = memcache.Client(['memcached:11211'], debug=0)
    mc.set("first_name", "Henrik")
    actual_name = mc.get("first_name")

    assert actual_name == "Henrik"
