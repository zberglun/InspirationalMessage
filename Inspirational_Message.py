# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 10:10:13 2024

@author: Zachary Berglund

@Purpose: This script is designed to be ran when desired and pop up an
inspirational quote. Perfect to provide motivation in a day where you are tired
or just feeling down.
"""

from random import *
import ctypes

quotes = ["You can really do whatever you want and accomplish whatever you want at any time in your life",
          "Perpetual optimisim is a fore multiplier" , "Be led by the dreams in your heart",
          "There is no substitute for hard work","To bring about change, you must not be afraid to take the first step",
          "Perfection is not attainable, but if we chase perfection we capture excellence",
          "It is never too late to be what you might have been", "Nothing is impossible, the word itself says i'm possible",
          "Hope is but the dream of those who wake", "It is in your moments of decision that your destiny is shaped",
          "What you do today can improve all your tommorows", " We aim above the mark to hit the mark",
          "If you can dream it, you can do it", "You are never too old to set another goal or to dream a new dream",
          "The most effective way to do it, is to do it", "It always seems impossible until it's done", 
          "Aim for the moon. If you miss, you may hit a star" "Shoot for the moon, if you don't make it there, the view will still be amazing",
          "There is nothing impossible to him who will try","Change your thoughts and you change your world",
          "You can't build a reputation on what you are going to do","A goal is a dream with a deadline" ]
message_box = ctypes.windll.user32.MessageBoxW
message_box(None,quotes[randint(0,len(quotes)-1)],"Today's Inspirational Message",0)