class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = nums1 + nums2
        sortedList = []
        l = []
        si = 0
        while len(nums3)>0:
            ks = nums3[0]
            for j in range(1,len(nums3)):
                if  ks>=nums3[j] :
                    ks = nums3[j]
                    si = j
            sortedList.append(ks)
            nums3.remove(ks)

        
        if len(sortedList) % 2 == 0:
            k = len(sortedList) / 2
            t = (sortedList[k-1] + sortedList[k])
            return float( t / 2.0)
        else:
             k = int(len(sortedList)) / 2
             return sortedList[k]
