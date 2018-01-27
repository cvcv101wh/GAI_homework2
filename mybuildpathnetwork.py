'''
 * Copyright (c) 2014, 2015 Entertainment Intelligence Lab, Georgia Institute of Technology.
 * Originally developed by Mark Riedl.
 * Last edited by Mark Riedl 05/2015
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
'''

import sys, pygame, math, numpy, random, time, copy, operator
from pygame.locals import *

from constants import *
from utils import *
from core import *

# Creates the path network as a list of lines between all path nodes that are traversable by the agent.
def myBuildPathNetwork(pathnodes, world, agent = None):
	lines = []
	### YOUR CODE GOES BELOW HERE ###
	uncheckedNodes = copy.copy(pathnodes)
	obsLines = world.getLines()
	while len(uncheckedNodes) > 0:
		for aNode in uncheckedNodes:
			if not (rayTraceWorld(uncheckedNodes[0],aNode,obsLines)):
				if uncheckedNodes[0]!=aNode:
					edgeCollidesFlag = True
					for aLine in obsLines:
						if (minimumDistance(aLine,uncheckedNodes[0]) <= agent.getMaxRadius()) or (minimumDistance(aLine,aNode) <= agent.getMaxRadius()) or (minimumDistance((uncheckedNodes[0],aNode),aLine[0]) <= agent.getMaxRadius()) or (minimumDistance((uncheckedNodes[0],aNode),aLine[1]) <= agent.getMaxRadius()):
								edgeCollidesFlag = False
					if edgeCollidesFlag:
						lines.append((uncheckedNodes[0],aNode))
											
		uncheckedNodes.pop(0)

	### YOUR CODE GOES ABOVE HERE ###
	return lines
