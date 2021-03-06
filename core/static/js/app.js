document.addEventListener("DOMContentLoaded", function() {
  /**
   * HomePage - Help section
   */
  class Help {
    constructor($el) {
      this.$el = $el;
      this.$buttonsContainer = $el.querySelector(".help--buttons");
      this.$slidesContainers = $el.querySelectorAll(".help--slides");
      this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
      this.init();
    }

    init() {
      this.events();
    }

    events() {
      /**
       * Slide buttons
       */
      this.$buttonsContainer.addEventListener("click", e => {
        if (e.target.classList.contains("btn")) {
          this.changeSlide(e);
        }
      });

      /**
       * Pagination buttons
       */
      this.$el.addEventListener("click", e => {
        if (e.target.classList.contains("btn") && e.target.parentElement.parentElement.classList.contains("help--slides-pagination")) {
          this.changePage(e);
        }
      });
    }

    changeSlide(e) {
      e.preventDefault();
      const $btn = e.target;

      // Buttons Active class change
      [...this.$buttonsContainer.children].forEach(btn => btn.firstElementChild.classList.remove("active"));
      $btn.classList.add("active");

      // Current slide
      this.currentSlide = $btn.parentElement.dataset.id;

      // Slides active class change
      this.$slidesContainers.forEach(el => {
        el.classList.remove("active");

        if (el.dataset.id === this.currentSlide) {
          el.classList.add("active");
        }
      });
    }

    /**
     * TODO: callback to page change event
     */
    changePage(e) {
      e.preventDefault();
      const page = e.target.dataset.page;

      console.log(page);
    }
  }
  const helpSection = document.querySelector(".help");
  if (helpSection !== null) {
    new Help(helpSection);
  }

  /**
   * Form Select
   */
  class FormSelect {
    constructor($el) {
      this.$el = $el;
      this.options = [...$el.children];
      this.init();
    }

    init() {
      this.createElements();
      this.addEvents();
      this.$el.parentElement.removeChild(this.$el);
    }

    createElements() {
      // Input for value
      this.valueInput = document.createElement("input");
      this.valueInput.type = "text";
      this.valueInput.name = this.$el.name;

      // Dropdown container
      this.dropdown = document.createElement("div");
      this.dropdown.classList.add("dropdown");

      // List container
      this.ul = document.createElement("ul");

      // All list options
      this.options.forEach((el, i) => {
        const li = document.createElement("li");
        li.dataset.value = el.value;
        li.innerText = el.innerText;

        if (i === 0) {
          // First clickable option
          this.current = document.createElement("div");
          this.current.innerText = el.innerText;
          this.dropdown.appendChild(this.current);
          this.valueInput.value = el.value;
          li.classList.add("selected");
        }

        this.ul.appendChild(li);
      });

      this.dropdown.appendChild(this.ul);
      this.dropdown.appendChild(this.valueInput);
      this.$el.parentElement.appendChild(this.dropdown);
    }

    addEvents() {
      this.dropdown.addEventListener("click", e => {
        const target = e.target;
        this.dropdown.classList.toggle("selecting");

        // Save new value only when clicked on li
        if (target.tagName === "LI") {
          this.valueInput.value = target.dataset.value;
          this.current.innerText = target.innerText;
        }
      });
    }
  }
  document.querySelectorAll(".form-group--dropdown select").forEach(el => {
    new FormSelect(el);
  });

  /**
   * Hide elements when clicked on document
   */
  document.addEventListener("click", function(e) {
    const target = e.target;
    const tagName = target.tagName;

    if (target.classList.contains("dropdown")) return false;

    if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
      return false;
    }

    if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
      return false;
    }

    document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
      el.classList.remove("selecting");
    });
  });

  /**
   * Switching between form steps
   */
  class FormSteps {
    constructor(form) {
      this.$form = form;
      this.$next = form.querySelectorAll(".next-step");
      this.$prev = form.querySelectorAll(".prev-step");
      this.$step = form.querySelector(".form--steps-counter span");
      this.currentStep = 1;

      this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
      const $stepForms = form.querySelectorAll("form > div");
      this.slides = [...this.$stepInstructions, ...$stepForms];

      this.init();
    }

    /**
     * Init all methods
     */
    init() {
      this.events();
      this.updateForm();
    }

    /**
     * All events that are happening in form
     */
    events() {
      // Next step
      this.$next.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep++;
          this.updateForm();
        });
      });

      // Previous step
      this.$prev.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep--;
          this.updateForm();
        });
      });

      // Form submit
      this.$form.querySelector("form").addEventListener("submit", e => this.submit(e));
    }

    /**Show span after chcekbox checked at STEP1*/


    /**
     * Update form front-end
     * Show next or previous section etc.
     */
    updateForm() {
      this.$step.innerText = this.currentStep;

      // TODO: Validation

      this.slides.forEach(slide => {
        slide.classList.remove("active");

        if (slide.dataset.step == this.currentStep) {
          slide.classList.add("active");
        }
      });

      this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
      this.$step.parentElement.hidden = this.currentStep >= 6;

      // TODO: get data from inputs and show them in summary
    }

    /**
     * Submit form
     *
     * TODO: validation, send data to server
     */
    submit(e) {
      e.preventDefault();
      this.currentStep++;
      this.updateForm();
    }
  }
  const form = document.querySelector(".form--steps");
  if (form !== null) {
    new FormSteps(form);
  }

  /** Shows span after checkbox checked step 1  */
  var checkboxes = document.querySelectorAll('.form-group.form-group--checkbox input[name="products[]"');
  for (cbox of checkboxes){
    cbox.addEventListener("change", function (e) {
      var span = this.parentElement.nextElementSibling;
      span.style.display = 'none';
      if (this.checked){
        span.style.display = 'block'
      }else{
        span.style.display = 'none'
      }
    e.preventDefault();
    })
  }
  /** Takes data from step 3a form,
   * then send them to server by ajax
   * and handle response with data*/

  $('#search').click(function (e) {
    e.preventDefault();
    var location = $('.form-group.form-group--dropdown div div').text();
    var for_who = "";
    checkboxes = $('input[name="help[]"]');
    for (let cbx of checkboxes){
      if (cbx.checked){
        for_who += cbx.nextElementSibling.textContent + ","
      }
    }
    var search = $('textarea[name="organization_search"]').val();
    $.ajax({
      url: 'ajax-load-charity',
      dataType: 'json',
      data: {
        'location': location,
        'for_who': for_who,
        'search': search,
      },
    }).done(function(response){
      var step = $('div[data-step="4"] h3');
      for (let item of response){
        var htmlElement = $(
          `<div class="form-group form-group--checkbox">
             <label>
               <input type="radio" name="organization" value="old"/>
               <span class="checkbox radio"></span>
               <span class="description">
                  <div class="title">${item.charity_name}</div>
                  <div class="subtitle">Cel i misja: ${item.help}</div>
                  <div class="subtitle">${item.location}</div>
               </span>
             </label>
           </div>`);
        step.after(htmlElement)
      }
    });
  });
  $('#summary').click(function (e) {
      e.preventDefault();

      /** inputs step 1 */
      var inputCheckboxes = $('input[name="products[]"]');
      var forWhoSummary = "";
      var value = "";
      var what_donate = "";
      for (let checkbox of inputCheckboxes){
            if (checkbox.checked){
                value = checkbox.value;
                what_donate = checkbox.nextElementSibling.nextElementSibling.textContent;
                console.log(what_donate);
                forWhoSummary += what_donate + ": ";
                var details = $(`input[name="products[${value}]"]`);
                if (value === 'toys'){
                    for (let det of details){
                        if (det.checked){
                            console.log(det.nextElementSibling.nextElementSibling.textContent);
                            forWhoSummary += det.nextElementSibling.nextElementSibling.textContent + "-";
                            var selects = det.parentElement.parentElement.nextElementSibling.firstElementChild.children;
                            for (let select of selects){
                                if (select.selected){
                                    console.log('SELECT');
                                    console.log(select.value);
                                    forWhoSummary += select.value + "; "
                                }
                            }
                        }

                    }forWhoSummary += "| "
                }else if(value === 'other'){
                    var textarea = $(`textarea[name="products[${value}]"]`).val();
                    forWhoSummary += textarea + " "
                }else {
                    for (let det of details){
                        if (det.checked){
                            console.log(det.nextElementSibling.nextElementSibling.textContent);
                            forWhoSummary += det.nextElementSibling.nextElementSibling.textContent + ", "
                        }
                    }
                    forWhoSummary += "| "
                }
            }
      }


      /** inputs step 2 */
      var bags = $('input[name="bags"]').val();
      console.log(`Liczba worków: ${bags}`);

      /** inputs step 4 */
      var charity = $('input[name="organization"]');
      for (let org of charity){
          if (org.checked){
              var organization = org.nextElementSibling.nextElementSibling.firstElementChild.textContent;
              var location = org.nextElementSibling.nextElementSibling.lastElementChild.textContent
          }
      }
      console.log(organization);
      console.log(location);

      /** inputs step 5 */

      var street = $('input[name="street"]').val();
      var city = $('input[name="city"]').val();
      var postcode = $('input[name="postcode"]').val();
      var phone = $('input[name="phone"]').val();
      var date = $('input[name="data"]').val();
      var time = $('input[name="time"]').val();
      var more_info = $('textarea[name="more_info"]').val();

      if (parseInt(bags) === 1){
          var bags_html = "worek"
      }else if (parseInt(bags) < 5){
          var bags_html = "worki"
      }else{
          var bags_html = "worków"
      }

      /** summary */

      var htmlBags = `
      <span class="summary--text">${bags} ${bags_html}: <strong>${forWhoSummary}</strong></span>`;
      var htmlCharity = `
      <span class="summary--text">Dla fundacji "${organization}" w ${location}</span>`;
      var htmlAddress = `
      <li>${street}</li>
      <li>${city}</li>
      <li>${postcode}</li>
      <li>${phone}</li>`;
      var htmlDate = `
      <li>${date}</li>
      <li>${time}</li>
      <li>Uwagi dla kuriera: ${more_info}</li>`;
      $('.icon.icon-bag').after(htmlBags);
      $('.icon.icon-hand').after(htmlCharity);
      $('#address').append(htmlAddress);
      $('#date').append(htmlDate);

      /** sendind data to server */
      $('#submit').click(function (e) {
          e.preventDefault();
          $.ajax({
              url: 'save-donate',
              data: {
                  'bags': bags,
                  'street': street,
                  'city': city,
                  'postcode': postcode,
                  'phone': phone,
                  'date': date,
                  'time': time,
                  'more_info': more_info,
                  'forWhoSummary': forWhoSummary,
                  'organization': organization,
              },
              method: 'get',
          }).done(function () {
              console.log('poszło')
          }).fail(function () {
              alert('Coś poszło nie tak')
          });
      });
      $(document).ajaxComplete(function () {
         $('div[data-step="6"]').removeClass("active");
         $('div[data-step="7"]').addClass('active');
      });
  });
});
