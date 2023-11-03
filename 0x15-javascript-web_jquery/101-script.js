#!/usr/bin/node
// script that adds, removes and clears LI elements from a list when the user clicks
$(document).ready(function () {
  const addItem = $('#add_item');
  const removeItem = $('#remove_item');
  const clearList = $('#clear_list');
  const myList = $('.my_list');

  addItem.click(function () {
    myList.append('<li>Item</li>');
  });

  removeItem.click(function () {
    myList.children().last().remove();
  });

  clearList.click(function () {
    myList.empty();
  });
});
