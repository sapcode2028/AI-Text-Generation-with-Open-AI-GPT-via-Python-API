import matplotlib.pyplot as plt
from collections import Counter
import re


response_1 = """
It seems the robot learning is going to end up being as complex as the actual learning. So if you take a little to learn about a toy, there’s one easy way to describe the process. The problem is the robot learning isn't a problem, but it's a problem that needs solving. There are so many different ways to describe the process.
But the simplest way to learn about a robot is to use data to describe a toy. This is the first approach to the problem. For example, imagine a toy with a human nose as a human head. Each human head is designed to be able to move around in a very similar manner, and that is a great way to describe the idea of an object in a room.
The solution is to call the object's "face". The robot will be able to use the object's face to understand the objects, and that is how it will learn about it.
The robot will then attempt to teach the object to move around in ways that can be seen in a room. This method could be used as a teaching method for the robot to perform a task. It could be used to teach the object to move in a room.
This method could be used as a teaching method.
"""

response_2 = """
This approach, in a nutshell, assumes that the goal is to meet all of the obligations of the government in order to get to the level where renewable energy is necessary in one paragraph. This approach assumes that the goals are only achievable through effective planning, in that respect, and in that respect the overall goal of the government is "to achieve all of the objectives achieved" in this paragraph and at the same time that it does not necessarily assume that it must always be achieved by "accelerating the pace" of development of the market at the time those goals are achieved.
The goal must be clear that if the goal is achieved (whether it is attained or not) the government needs to be aware of the real cost of its development. It must give the government every opportunity to make a contribution to the market and to enable "accelerating the pace" of development in order to support its growth.
"""

def get_word_frequencies(text):
    text = text.lower()
    words = re.findall(r'\b[a-z]+\b', text)  
    return Counter(words)


freq1 = get_word_frequencies(response_1)
freq2 = get_word_frequencies(response_2)


top1 = freq1.most_common(10)
top2 = freq2.most_common(10)


words1, counts1 = zip(*top1)
words2, counts2 = zip(*top2)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.bar(words1, counts1, color='skyblue')
plt.title('Top 10 Word Frequencies: Robot Learning Response')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')

plt.subplot(1, 2, 2)
plt.bar(words2, counts2, color='lightgreen')
plt.title('Top 10 Word Frequencies: Renewable Energy Response')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()
