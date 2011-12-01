#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import uuid
import leveldb

def main():
	n=10000
	print("%s: write %d items to db.."%(datetime.datetime.now(),n))
	
	db = leveldb.LevelDB("./leveldb.db")
	for i in range(n):
		db.Put(str(i), "this is item %d"%(i))
		
		
	print("%s: lookup a item from map..."%(datetime.datetime.now()))
	print(db.Get("43"))
	print("%s: ok"%(datetime.datetime.now()))
	
	return 0

if __name__ == '__main__':
	main()
