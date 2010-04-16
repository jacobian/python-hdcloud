from __future__ import absolute_import

from hdcloud import Job
from .fakeserver import FakeHDCloud
from .utils import assert_isinstance
from nose.tools import assert_equal

hdcloud = FakeHDCloud()

def test_all():
    hdcloud.jobs.all()
    hdcloud.assert_called('GET', '/jobs.json?page=1')
    hdcloud.jobs.all(page=2)
    hdcloud.assert_called('GET', '/jobs.json?page=2')
    
def test_current():
    hdcloud.jobs.current()
    hdcloud.assert_called('GET', '/jobs/current.json?page=1')
    hdcloud.jobs.current(page=2)
    hdcloud.assert_called('GET', '/jobs/current.json?page=2')
    
def test_completed():
    hdcloud.jobs.completed()
    hdcloud.assert_called('GET', '/jobs/completed.json?page=1')
    hdcloud.jobs.completed(page=2)
    hdcloud.assert_called('GET', '/jobs/completed.json?page=2')

def test_failed():
    hdcloud.jobs.failed()
    hdcloud.assert_called('GET', '/jobs/failed.json?page=1')
    hdcloud.jobs.failed(page=2)
    hdcloud.assert_called('GET', '/jobs/failed.json?page=2')

def test_get():
    hdcloud.jobs.get(id=1)
    hdcloud.assert_called('GET', '/jobs/1.json')
    
def test_frames():
    job = hdcloud.jobs.get(id=1)
    job.frames()
    hdcloud.assert_called('GET', '/jobs/1/frames.json?page=1')
    job.frames(page=2)
    hdcloud.assert_called('GET', '/jobs/1/frames.json?page=2')
    
def test_delete():
    job = hdcloud.jobs.get(id=1)
    job.delete()
    hdcloud.assert_called('DELETE', '/jobs/1.json')
    
def test_destroy_bulk():
    hdcloud.jobs.destroy_bulk([1, 2, 3])
    hdcloud.assert_called('DELETE', '/jobs/destroy_bulk.json?job_ids%5B%5D=1&job_ids%5B%5D=2&job_ids%5B%5D=3')
    
def test_job_repr():
    assert_equal(str(hdcloud.jobs.get(id=1)), '<Job: 1 - Encoding: Pass 1>')
    
def test_job_create():
    st = hdcloud.stores.get(id=1)
    pr = hdcloud.profiles.get(id=1)
    jobs = hdcloud.jobs.create(
        source = st,
        destination = st,
        files = ['hi.mpg'],
        profiles = [pr],
    )
    assert_isinstance(jobs[0], Job)