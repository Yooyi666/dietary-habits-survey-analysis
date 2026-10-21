# Execute from the repository root with an authorised local CSV.
path <- "survey_data.csv"
if (!file.exists(path)) stop("Local survey_data.csv is required.")
d <- read.csv(path, stringsAsFactors = FALSE)
stopifnot(nrow(d) == 107L, ncol(d) == 19L)
stopifnot(all(c("Lunch", "Gender") %in% names(d)))
stopifnot(is.numeric(d$Lunch), !anyNA(d$Lunch))
stopifnot(all(d$Lunch %in% 0:7), all(d$Lunch == as.integer(d$Lunch)))
stopifnot(!anyNA(d$Gender), all(nzchar(trimws(d$Gender))))
stopifnot(identical(as.integer(table(factor(d$Lunch, levels=0:7))),
                    c(1L, 0L, 1L, 1L, 6L, 15L, 17L, 66L)))
stopifnot(identical(sort(as.integer(table(d$Gender))), c(1L, 27L, 79L)))
cat("LUNCH VALIDATION: PASS\n")
