#!/usr/bin/env python2.7
import sys


from filterdup import cal_max_dup_tags
from cProb import binomial_cdf_inv, binomial_pdf
##
##cpdef binomial_cdf_inv ( double cdf, long a, double b ):
##    """BINOMIAL_CDF_INV inverts the binomial CDF. For lower tail only!
##
##    """
##    if cdf < 0 or cdf >1:
##        raise Exception("CDF must >= 0 or <= 1")
##
##    cdef double cdf2 = 0
##    cdef long x
##
##    for x in xrange(0,a+1):
##        pdf = binomial_pdf (x,a,b)
##        cdf2 = cdf2 + pdf
##        if cdf < cdf2:
##            return x
##    return a
##
##
##cpdef binomial_pdf( long x, long a, double b ):
##    """binomial PDF by H. Gene Shin
##    
##    """
##    
##    if a<1:
##        return 0
##    elif x<0 or a<x:
##        return 0
##    elif b==0:
##        if x==0:
##            return 1
##        else:
##            return 0
##    elif b==1:
##        if x==a:
##            return 1
##        else:
##            return 0
##
##    cdef double p
##    cdef long mn
##    cdef long mx
##    cdef double pdf
##    cdef long t
##    cdef long q
##
##    if x>a-x:
##        p=1-b
##        mn=a-x
##        mx=x
##    else:
##        p=b
##        mn=x
##        mx=a-x
##    pdf=1
##    t = 0
##    for q in xrange(1,mn+1):
##        pdf*=(a-q+1)*p/(mn-q+1)
##        if pdf < 1e-100:
##            while pdf < 1e-3:
##                pdf /= 1-p
##                t-=1
##        if pdf > 1e+100:
##            while pdf > 1e+3 and t<mx:
##                pdf *= 1-p
##                t+=1
##
##    for i in xrange(mx-t):
##        pdf *= 1-p
##        
##    pdf=float("%.10e" % pdf)
##    return pdf
##
##
##def cal_max_dup_tags ( genome_size, tags_number, p=1e-5 ):
##    """Calculate the maximum duplicated tag number based on genome
##    size, total tag number and a p-value based on binomial
##    distribution. Brute force algorithm to calculate reverse CDF no
##    more than MAX_LAMBDA(100000).
##    
##    """
##    return binomial_cdf_inv(1-p,tags_number,1.0/genome_size)
##
##

if len(sys.argv) == 1:
    print
    print "Usage: pyscript genome_size numTags p-value"
    print
    print
    quit()

genome_size = float(sys.argv[1])
tags_number = float(sys.argv[2])
p = float(sys.argv[3])
maxtags=cal_max_dup_tags (genome_size, tags_number, p)

print maxtags
