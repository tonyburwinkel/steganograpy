import unittest
from unittest import TestCase
from tickets import make_prequeue, ticket_sim
from queue import Queue

class test_text_convert(TestCase):
    '''
		this class tests the methods in the text convert module
    '''
    def test_(self):
        '''
        '''
        q = Queue(20)
        self.assertEqual(q.start,0)
        self.assertEqual(q.end,0)
        for i in range(20):
            q.enqueue(i)
        self.assertEqual(q.enqueue(1),0) # make sure the queue is full and returns 0
        for i in range(10):
            q.dequeue()
        self.assertTrue(q.enqueued < q.size) # make sure the queue's enqueued variable has decremented
        self.assertTrue(q.start == 10) # make sure the start has moved
        for i in range(10):
            q.enqueue(i)
        self.assertTrue(q.end == q.start) # make sure the end is wrapping around the buffer
        self.assertTrue(q.is_full()) # test the queue's is_full method
        for i in range(20):
            q.dequeue()
        self.assertTrue(q.end == q.start) # make sure the start is wrapping around the buffer
        self.assertTrue(q.dequeue() == 0)
        self.assertTrue(q.is_empty())

if __name__=="__main__":
	unittest.main()
