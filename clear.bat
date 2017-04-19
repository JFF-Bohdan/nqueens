@echo Removing Python compiled files...

@set DIRS_TO_RD=(.\__pycache__ .\system\__pycache__ .\tests\__pycache__)

@for %%i in %DIRS_TO_RD% do @(
	@if exist %%i (
	    @attrib -r -s -h %%i
		@del /F /Q  %%i\*
		@echo     Removing: %%i
		@rmdir /Q /S %%i > nul
	)
)

@echo Done
