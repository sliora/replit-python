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
        while steps > 0 and self.current.next is not None:
            steps -= 1
            self.current = self.current.next
        return self.current.val


history = BrowserHistory("leetcode.com")
history.visit("google.com")
history.visit("facebook.com")
history.visit("youtube.com")
history.back(1)
history.back(1)
history.forward(1)
history.visit("linkedin.com")
history.forward(2)
history.back(2)
history.back(7)

print(history.current.val)

