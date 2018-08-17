import ToolsOutput
from ToolsOutput import ToolsOutput_Class

class ToolsScreen_Class:
    def Make_Empty_Lines(number_of_empty_lines):
        for empty_lines_counter in range(number_of_empty_lines):
            ToolsOutput.ToolsOutput_Class.PrintStringOnSeperateLine("")
            #ToolsOutput_Class.PrintStringOnSeperateLine("")
            #Syntaksen for linjen herover kan også bruges, når vi også har linje 2 (herover) med !!!