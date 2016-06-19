import time
from espeak import espeak
import cv2
import numpy as np
from PyDictionary import PyDictionary
#import abc2
#import sys
#sys.path.insert(0, "/home/sam/Desktop")
#from itsp import abc2

def dictionary(word):
	i=0
	while (1):
	
		dictionary=PyDictionary()
		dict=dictionary.meaning(word)

		if (dict.has_key('Adjective')) :
	
			s= dict['Adjective']
			if len(s)>=i :
				print s[i] 	
				l= len(s[i])
				t = l /12.0
				espeak.synth("(adjective)" + s[i])
				time.sleep(t)
		if dict.has_key('Noun') :
			s= dict['Noun']
			if len(s)>=i :
				print s[i] 	
				l= len(s[0])
				t = l /12.0
				espeak.synth("(NOUN)" + s[i])
				time.sleep(t)
		if dict.has_key('Verb') :
			s= dict['Verb']
			if len(s)>=i :
				print s[i] 
				l= len(s[i])
				t = l /12.0
				espeak.synth("VERB" + s[i])
				time.sleep(t)
		if dict.has_key('Adverb') :
			s= dict['Adverb']
			if len(s)>=i :
				print s[i] 
				l= len(s[i])
				t = l /12.0
				espeak.synth("(ADVERB)" + s[i])
				time.sleep(t)
		if dict.has_key('Preposition') :
			s= dict['Preposition']
			if len(s)>=i :
				print s[i] 
				l= len(s[i])
				t = l /12.0
				espeak.synth("(PREPO)" + s[i])
				time.sleep(t)
		espeak.synth("If alternate meaning required, give a double tap within the next 3 seconds")
		#audio trigger will be awaited here, after message for one, in case user didnt get meaning that was wanted
		#if received, then i++
