import pytumblr

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  'R23DpvtZwrwJ7A2VeVxpv5rzHzjEXbH8IFh2JGe27DkCHqA0gv',
  'jKPESRNXi0C0NjRvX1AnzoWn3dDGNCY8JQIfO8zH6BZNOAkcnH',
  'Y1vxY4c4hSQSfjFgRrKqhKMdSEJNAvuaoST7y7HvPWlGWCna9E',
  'KZUMhEflAVVWBadS8cxYvGibRY1HJK1XT9K1PFD9IvrB4mCxFD'
)

# Make the request
print(client.info())