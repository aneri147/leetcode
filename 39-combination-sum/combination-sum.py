class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # res = []
        # def backtrack(start, path, total):
        #     if total == target:
        #         res.append(path[:])
        #     if total > target:
        #         return
        #     for i in range(start, len(candidates)):
        #         path.append(candidates[i])
        #         backtrack(i, path, total + candidates[i])
        #         path.pop()

        # backtrack(0, [], 0)
        # return res

        # res = []
        # def backtrack(start, path, total):
        #     if total == target:
        #         res.append(path[:])
        #     if total > target:
        #         return
        #     for i in range(start, len(candidates)):
        #         path.append(candidates[i])
        #         backtrack(i, path, total +candidates[i])
        #         path.pop()
        # backtrack(0, [], 0)
        # return res



        # res = []
        
        # def backtrack(start, path, total):
        #     if total == target:
        #         res.append(path[:])
        #     if total > target:
        #         return
        #     for i in range(start, len(candidates)):
        #         path.append(candidates[i])
        #         backtrack(i, path, total + candidates[i])
        #         path.pop()

        # backtrack(0,[],0)
        # return res

        # res = []
        # def backtrack(start,path,total):
        #     if total == target:
        #         res.append(path[:])
        #     if total > target:
        #         return
        #     if total < target:
        #         for i in range(start, len(candidates)):
        #             path.append(candidates[i])
        #             backtrack(i,path,total+candidates[i])
        #             path.pop()
        # backtrack(0,[],0)
        # return res

        # res = []
        # def backtrack(start, path, total):
        #     if total == target:
        #         res.append(path[:])
        #     if total < target:
        #         for i in range(start, len(candidates)):
        #             path.append(candidates[i])
        #             backtrack(i,path,total+candidates[i])
        #             path.pop()
        #     if total > target:
        #         return
        # backtrack(0,[],0)
        # return res
        

#         res=[]
#         def back(i,path,total):
#             if total>target:
#                 return
#             if total==target:
#                 res.append(path[:])
#             back(i+1,path,total)
#             path=path+candidates[i]
#             back(i,path,total+candidates[i])
#             path.pop()
#             return
            

        
#             back(i,[],0)


    


#     res = []

# def back(i, path, total):
#     if total > target:
#         return
#     if total == target:
#         res.append(path)
#         return
    
#     if i >= len(candidates):
#         return

#     # option 1: skip current candidate
#     back(i+1, path, total)

#     # option 2: use current candidate (create a new list, not in-place)
#     back(i+1, path + [candidates[i]], total + candidates[i])  

# back(0, [], 0)

        # res = []
        # def backtrack(index,path,total):
        #     if total == target:
        #         res.append(path[:])
        #     if total < target:
        #         for i in range(index, len(candidates)):
        #             path.append(candidates[i])
        #             backtrack(i, path, total + candidates[i])
        #             path.pop()
        #     if total > target:
        #         return

        # backtrack(0, [], 0)
        # return res






        # res = []
        # total = 0
        # def backtrack(index, total, path):
        #     if target == total:
        #         res.append(path[:])
        #     if total < target:
        #         for i in range(index, len(candidates)):
        #             path.append(candidates[i])
        #             backtrack(i, total + candidates[i], path)
        #             path.pop()
        #     if total > target:
        #         return
        # backtrack(0, 0, [])
        # return res

        # res = []
        # def backtrack(start, total, path):
        #     if total == target:
        #         res.append(path[:])
        #     if total < target:
        #         for i in range(start, len(candidates)):
        #             path.append(candidates[i])
        #             backtrack(i, total + candidates[i], path)
        #             path.pop()
        #         if total > target:
        #             return
        #         backtrack
        #     return res

        res = []
        total = 0
        def backtrack(start, path, total):
            if target == total:
                res.append(path[:])
            elif target < total:
                return
            elif target > total:
                for i in range(start, len(candidates)):
                    path.append(candidates[i])
                    backtrack(i, path, total + candidates[i])
                    path.pop()
        backtrack(0, [], 0)
        return res
