# Execute from the repository root with an authorised local CSV.
path <- "survey_data.csv"
if (!file.exists(path)) stop("Local survey_data.csv is required.")
d <- read.csv(path, stringsAsFactors = FALSE)
stopifnot(nrow(d) == 107L, ncol(d) == 19L)
stopifnot(all(c("Breakfast", "Employment") %in% names(d)))
stopifnot(is.numeric(d$Breakfast), !anyNA(d$Breakfast))
stopifnot(all(d$Breakfast %in% 0:7), all(d$Breakfast == as.integer(d$Breakfast)))
stopifnot(!anyNA(d$Employment), all(nzchar(trimws(d$Employment))))
stopifnot(identical(as.integer(table(factor(d$Breakfast, levels=0:7))),
                    c(2L, 1L, 5L, 8L, 10L, 12L, 7L, 62L)))
stopifnot(identical(sort(as.integer(table(d$Employment))),
                    c(3L, 3L, 4L, 12L, 14L, 16L, 55L)))
cat("BREAKFAST VALIDATION: PASS\n")
