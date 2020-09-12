#Find
import playerSettingModule

#Add
IsLoaded = False
	
#Find
		self.__SetProgress(0)
		
#Add Above		
		global IsLoaded
		if not IsLoaded:
			tmpLoadStepList = tuple(zip(*self.loadStepList))[0]
			for progress in set(range(tmpLoadStepList[0], tmpLoadStepList[-1] + 1)).difference(tmpLoadStepList):
				self.loadStepList.append((progress, lambda: None))
			self.loadStepList.sort()
			IsLoaded = True