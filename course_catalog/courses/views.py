from django.shortcuts import render, get_object_or_404, redirect
from .forms import CourseForm

from .models import Course, Cart


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form})


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'courses/course_confirm_delete.html', {'course': course})


def add_to_cart(request, pk):
    course = get_object_or_404(Course, pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.courses.add(course)
    return redirect('cart_detail')


def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'courses/cart_detail.html', {'cart': cart})


def remove_from_cart(request, pk):
    course = get_object_or_404(Course, pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.courses.remove(course)
    return redirect('cart_detail')
