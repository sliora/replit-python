class LinkedNode(object):
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory(object):
    def __init__(self, homepage):
        self.head = self.current = LinkedNode(homepage)

    def visit(self, url):
        self.current.next = LinkedNode(url, prev=self.current)
        self.current = self.current.next
        return None
    def back(self, steps):
        while steps > 0 and self.current.prev is not None:
            steps -= 1
            self.current = self.current.prev
        return self.current.val
    def forward(self, steps):
        """
        type steps: int
        rtype: str
        """


history = BrowserHistory("leetcode.com")
history.visit("google.com")
history.visit("facebook.com")
history.visit("youtube.com")
print(history.head.next.val)
print(history.current.next)
print(history.current.val)
print(history.current.prev.val)
print(history.back(5))