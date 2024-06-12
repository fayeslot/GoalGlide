import string, random 
from django.db.models.signals import pre_save 
from django.dispatch import receiver 
from django.utils.text import slugify

def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits): 
	return ''.join(random.choice(chars) for _ in range(size)) 

def unique_slug_generator(instance, new_slug = None): 
	if new_slug is not None: 
		slug = new_slug 
	else: 
		slug = slugify(instance.name) 
	Klass = instance.__class__ 
	max_length = Klass._meta.get_field('slug').max_length 
	slug = slug[:max_length] 
	qs_exists = Goal.objects.filter(slug = slug).exists() 
	
	if qs_exists: 
		new_slug = "{slug}-{randstr}".format( 
			slug = slug[:max_length-5], randstr = random_string_generator(size = 4)) 
			
		return unique_slug_generator(instance, new_slug = new_slug) 
	return slug
#def addGoal(request):
 #   if request.method == 'POST':
  #      form = AddForm(request.POST)
   #     if form.is_valid():
    #        goal = form.save(commit=False)  # Save the form but don't commit yet
     #       goal.user = request.user  # Assign the logged-in user (assuming request.user is available)
      #      goal.save()  # Now commit the changes to the database
       #     messages.success(request, 'Goal added successfully!')  # Display success message (optional)
        #    return redirect('goals')  # Redirect to goals page after saving
        #else:
         #   return render(request, 'goals/addgoal.html', {'form': form, 'error': 'Form is invalid'})
    #else:
     #   form = AddForm()
    #return render(request, 'goals/addgoal.html', {'form': form})