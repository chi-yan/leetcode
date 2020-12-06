        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if nums1 == [] or nums2 == []:
            return []
        nums1.sort()
        nums2.sort()
        count = 0
        i = 0
        j = 0
        heap = []
        heapq.heappush(heap, (nums1[i] + nums2[j], i, j))
        ans = []
        seen = set((0,0))
        while count < k and heap:
            _, i, j = heapq.heappop(heap)
            ans.append([nums1[i],nums2[j]])
            count += 1
   #             print(count)
   #             print(str(i) + " " + str(j) + " " + str(ans))
            if i < len(nums1)-1 and (i+1,j) not in seen:
                heapq.heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
                seen.add((i+1,j))
            if j < len(nums2)-1 and (i,j+1) not in seen:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
                seen.add((i,j+1))
        return ans
            
