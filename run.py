from nlprecipes import main

Options = [["vegetarian to meat","vegetarian_to_meat"],
            ["meat to vegetarian","meat_to_vegetarian"],
            ["healthy to unhealthy","healthy_to_unhealthy"],
            ["unhealthy to healthy", "unhealthy_to_healthy"],
            ["to Chinese", "Chinese"],
            ["to Italian", "Italian"],
            ["to Korean", "Korean"],
            ["to Indian", "Indian"],
            ["to Mexican", "Mexican"],]
def run():
  recipeURL = raw_input(" '1':southwest chicken casserole\n '2':filet mignon with balsamic glaze\n '3':artichoke spinach dip\n '4':quick and easy jambalaya\n Please enter a URL to a recipe or select an option from the list above: ")
  if (recipeURL == '1'):
    recipeURL = "http://allrecipes.com/recipe/231173/spicy-southwest-chicken-casserole"
  elif (recipeURL == '2'):
    recipeURL = "http://allrecipes.com/recipe/30578/filet-mignon-with-rich-balsamic-glaze"
  elif (recipeURL == '3'):
    recipeURL = "http://allrecipes.com/recipe/33474/artichoke-spinach-dip-restaurant-style"
  elif (recipeURL == '4'):
    recipeURL = "http://allrecipes.com/recipe/236995/quick-and-easy-jambalaya"
  print "\n using URL:\n [", recipeURL,"]\n"
  valid_transformation = False
  initialPrintOption = ""

  while (not valid_transformation):
    initialPrintOption = raw_input(" '1':No\n '2':Print with Object Notation\n '3':Print Human Readable Notation\n '4':Both \n Do you want to print the initial recipe?: ")
    if (initialPrintOption == '1'):
      initialPrintOption = "No"
      valid_transformation = True
    elif (initialPrintOption == '2'):
      initialPrintOption = "Object"
      valid_transformation = True
    elif (initialPrintOption == '3'):
      initialPrintOption = "Human"
      valid_transformation = True
    elif (initialPrintOption == '4'):
      initialPrintOption = "Both"
      valid_transformation = True
    else:
      print "Invalid option, please enter a number from 1 to 4 \n"

  print '\n'
  recipe = main.parse(recipeURL)

  if initialPrintOption == 'Object' or initialPrintOption == 'Both':
    print recipe.object_notation()
  if initialPrintOption == 'Human' or initialPrintOption == 'Both':
    print '\n'
    print recipe.human_readable()

  print '\n'
  valid_transformation = False
  transformation = ""
  while (not valid_transformation):
    inputStr = ""
    num = 1
    for x in Options:
      inputStr = inputStr + '\'' + str(num) + '\':' + x[0] + '\n'
      num += 1
    inputStr = inputStr + "Enter a Transformation Option: "
    transformation = raw_input(inputStr)

    if transformation.isdigit():
      index = int(transformation) - 1
      if index >= 0 and index < len(Options):
        valid_transformation = True
        transformation = Options[index][1]
    else:
      print "Invalid option, please enter a number from 1 to ", str(len(Options)) , "\n"

  print "transformation: ", transformation

  valid_transformation = False
  finalPrintOption = ""
  print '\n'

  while (not valid_transformation):
    finalPrintOption = raw_input(" '1':No\n '2':Print with Object Notation\n '3':Print Human Readable Notation\n '4':Both\n Do you want to print the transformed recipe?: ")
    if (finalPrintOption == '1'):
      finalPrintOption = "No"
      valid_transformation = True
    elif (finalPrintOption == '2'):
      finalPrintOption = "Object"
      valid_transformation = True
    elif (finalPrintOption == '3'):
      finalPrintOption = "Human"
      valid_transformation = True
    elif (finalPrintOption == '4'):
      finalPrintOption = "Both"
      valid_transformation = True
    else:
      print "Invalid option, please enter a number from 1 to 4 \n"

  print '\n'
  main.transform(recipe, transformation)

  if finalPrintOption == 'Object' or finalPrintOption == 'Both':
    print recipe.object_notation()
  if finalPrintOption == 'Human' or finalPrintOption == 'Both':
    print '\n'
    print recipe.human_readable()

if __name__ == '__main__':
  run()
