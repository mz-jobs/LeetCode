class Twitter(object):

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.tweets = []
    self.following = {}
    self.unfollowingSELF = set()

  def postTweet(self, userId, tweetId):
    """
    Compose a new tweet.
    :type userId: int
    :type tweetId: int
    :rtype: None
    """
    self.tweets.append((userId, tweetId))

  def getNewsFeed(self, userId):
    """
    Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
    :type userId: int
    :rtype: List[int]
    """
    # users = set()
    # if userId not in self.unfollowingSELF:
    users = set([userId])

    if userId in self.following:
      users |= self.following[userId]
    return [t[1] for t in self.tweets if t[0] in users][:-11:-1]

  def follow(self, followerId, followeeId):
    """
    Follower follows a followee. If the operation is invalid, it should be a no-op.
    :type followerId: int
    :type followeeId: int
    :rtype: None
    """
    # if followerId == followeeId:
    #   self.unfollowingSELF.discard(followerId)

    if followerId not in self.following:
      self.following[followerId] = set([followeeId])
    else:
      self.following[followerId].add(followeeId)

  def unfollow(self, followerId, followeeId):
    """
    Follower unfollows a followee. If the operation is invalid, it should be a no-op.
    :type followerId: int
    :type followeeId: int
    :rtype: None
    """
    # if followerId == followeeId:
    #   self.unfollowingSELF.add(followerId)
    if followerId in self.following:
      self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
print(obj.getNewsFeed(1))
obj.follow(1, 2)
obj.postTweet(2, 6)
print(obj.getNewsFeed(1))
obj.unfollow(1, 2)
obj.unfollow(1, 2)
obj.unfollow(1, 1)
print(obj.getNewsFeed(1))
