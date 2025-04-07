from django.shortcuts import render
from .forms import BudgetForm


def budget_view(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BudgetForm()
    return render(request, 'budget/budget.html', {'form': form})
